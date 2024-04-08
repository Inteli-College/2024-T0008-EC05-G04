import asyncio
import asyncpg
from tokens import DATABASE_URL
import nest_asyncio

nest_asyncio.apply()


class ConnPostgres:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            try:
                instance = super(ConnPostgres, cls).__new__(cls)
                asyncio.run(instance._init_connection())
                cls._instance = instance
            except Exception as e:
                print(f"Initial database connection failed: {e}")
                cls._instance = None  # Reset the instance to allow future retries
        return cls._instance

    async def _init_connection(self):
        self.__database_url = DATABASE_URL

        # print(f"Connecting to database at {self.__database_url}")

        self.conn = None

        if not await self.start_conn():
            raise Exception(
                "Unable to connect to database, please check your credentials"
            )
        else:
            print("Database connection established")

    async def start_conn(self) -> bool:
        try:
            print("Connecting to database...")
            self.conn = await asyncpg.connect(self.__database_url)
            await self.conn.execute("SET TIME ZONE 'America/Sao_Paulo'")
            return True
        except Exception as e:
            print(f"Database connection error: {e}")
            self.conn = None
            return False

    async def close_conn(self):
        if self.conn:
            await self.conn.close()
            self.conn = None

    async def is_connection_open(self) -> bool:
        if not self.conn:
            return False

        try:
            async with self.conn.transaction():
                await self.conn.fetch("SELECT 1")
                return True
        except:
            return False

    def __getattr__(self, name):
        loop = asyncio.get_event_loop()
        if str(name) == "conn":
            return self.conn

        if self.conn is not None:
            if loop.run_until_complete(self.is_connection_open()):
                return getattr(self.conn, name)
            else:
                loop.run_until_complete(self.close_conn())
                if loop.run_until_complete(self.start_conn()):
                    return getattr(self.conn, name)
                else:
                    raise Exception(
                        "Fatal error during reconnection attempt, maybe database down?"
                    )
        else:
            raise Exception("Connection object is not initialized")

    def __repr__(self):
        return repr(self.conn)


# Singleton instance creation
conn_postgres = ConnPostgres()
