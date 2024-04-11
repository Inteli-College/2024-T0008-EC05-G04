import Navbar from "./navbar";
import PropTypes  from "prop-types";

interface PageProps {
    children: React.ReactNode;
}

const Page: React.FC<PageProps> = ({children}) => {
    return(
        <>
            <Navbar />
            <main className="bg-gray-100 mt-0">{children}</main>
        </>
    )
}

Page.propTypes = {
    children: PropTypes.node.isRequired,
}

export default Page