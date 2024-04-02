import React, { useState } from 'react';

export interface HamburgerProps {
    /** Callback function, which should be executed on click */
    onClick: () => void;

    /** Initial state of our button */
    isInitiallyOpen?: boolean;
}

export function Hamburger(props: HamburgerProps) {
    const { onClick, isInitiallyOpen } = props;
    const [isOpen, setIsOpen] = useState<boolean>(isInitiallyOpen ?? false);

    const handleClick = () => {
        setIsOpen((prev) => !prev);
        onClick();
    };

    return (
        <button
            onClick={handleClick}
            type="button"
            className={`w-8 h-8 flex justify-around flex-col flex-wrap z-10 cursor-pointer`}
        >
            <div
                className={`bg-white block w-8 h-[0.40rem] transition-all origin-[1px] ${
                    isOpen ? 'rotate-45' : 'rotate-0'
                }`}
            />
            <div
                className={`bg-white block w-8 h-[0.40rem] transition-all origin-[1px] ${
                    isOpen ? 'translate-x-full bg-transparent' : 'translate-x-0'
                }`}
            />
            <div
                className={`bg-white block w-8 h-[0.40rem] transition-all origin-[1px] ${
                    isOpen ? 'rotate-[-45deg]' : 'rotate-0'
                }`}
            />
        </button>
    );
}

{/* Hamburger button */}
/*<div className='me-5'>
<Hamburger onClick={handleHamburgerClick} isInitiallyOpen={false} />
</div>
{isMenuOpen && (
    <div className="w-2/12 bg-navblue absolute items-center right-0 rounded-b-lg">
    <ul className="flex flex-col mt-4 space-y-2">
        <li><a href="/" className="text-white text-lg block p-2">Home</a></li>
        <li><a href="#services" className="text-white text-lg block p-2">Services</a></li>
        <li><a href="#about" className="text-white text-lg block p-2">About</a></li>
        <li><a href="#contact" className="text-white text-lg block p-2">Contact</a></li>
    </ul>
    </div>

    )}*/
