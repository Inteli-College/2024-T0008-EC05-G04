import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // Import useNavigate
import Sirio from '../static/logoS.svg'
import Logo from '../static/logo.svg'

const Login: React.FC = () => {
  const navigate = useNavigate(); // Initialize the navigate function
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    // Implement the login logic here
  };

  const handleLoginClick = (path: string) => {
    navigate(path);
  };

  return (
    
    <div className="flex h-screen">
      <div className="w-2/5 bg-navblue flex justify-center items-center">
        <div className="text-white">
          <img src={Sirio} alt="Hospital Sírio Libanês" />
        </div>
      </div>
      

      {/* Right side with the form */}
      <div className="w-3/5 bg-white flex justify-center items-center">
        <div className="bg-white rounded-lg space-y-20">
          <img className="mb-10 w-full" src={Logo} alt="Logo" />
          <form className="space-y-10" onSubmit={handleLogin}>
            <input
              type="text"
              placeholder="Email"
              className="w-full text-xl px-4 py-3 rounded-xl bg-txtg"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
            <input
              type="password"
              placeholder="Senha"
              className="w-full text-xl px-4 py-3 rounded-xl bg-txtg" 
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <div className="flex flex-col justify-center items-center space-y-10">
              <button
                className="underline hover:text-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
                onClick={() => handleLoginClick('/menu')}
                type="button"
              >
                Esqueci minha senha
              </button>
              <button
                type="submit"
                className="w-6/12 text-xl bg-greyb text-white px-6 py-3 rounded-xl hover:bg-navblue transition duration-300"
                onClick={() => handleLoginClick('/menu')}
              >
                Login
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Login;