import React from "react";
import Logo from "../assets/Logo.svg"
import { Link } from "react-router-dom";

const Navbar = () => {
  return(
    <>
      <nav className="top-0 left-0 riht-0 bg-pink-600 fixed w-full z-20 shadow shadow-rose-700">
        <div className="max-w-screen-xl flex justify-between flex-wrap items-center mx-auto mr-4 p-4">
          <a href="/" className="flex items-center">
            <img
              src={Logo}
              className="h-10 mr-3"
              alt="Dreamjob Logo"
            />
          </a>

          <div className="place-items-center flex md:order-2">
            <button
              data-collapse-toggle="navbar-sticky"
              type="button"
              className="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-pink-100 rounded-lg md:hidden hover:bg-pink-500 focus:outline-none focus:ring-2 focus:ring-gray-200 "
              aria-controls="navbar-sticky"
              aria-expanded="false"
            >
              <span className="sr-only">Open main menu</span>
              <svg
                className="w-6 h-6 items-center"
                aria-hidden="true"
                fill="currentColor"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
              >
                <path
                  fillRule="evenodd"
                  clipRule="evenodd"
                  stroke="currentColor"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M1 1h15M1 7h15M1 13h15"
                />
              </svg>
            </button>
          </div>

          <div class="hidden w-full md:block md:w-auto md:order-1" id="navbar-sticky">
            <ul class="flex flex-col p-4 md:p-0 mt-4 font-medium border border-gray-100 rounded-lg bg-transparent md:flex-row md:space-x-8 md:mt-0 md:border-0 md:bg-transparent dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700">
              <li>
                <a href="/" class="block py-2 pl-3 pr-4  text-white rounded hover:text-[#87CED0] md:hover:bg-transparent md:hover:text-[#87CED0] md:p-0 ">
                  Home
                </a>
              </li>
              <li>
                <a href="/job-vacancy" class="block py-2 pl-3 pr-4  text-white rounded hover:text-[#87CED0] md:hover:bg-transparent md:hover:text-[#87CED0] md:p-0 ">
                  Job Vacancy
                </a>
              </li>
              <li>
                <a href="/" class="block py-2 pl-3 pr-4  text-white rounded hover:text-[#87CED0] md:hover:bg-transparent md:hover:text-[#87CED0] md:p-0 ">
                  Contact
                </a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </>
  )
}
export default Navbar

// const Navbar = () => {
//   return (
//     <>
//       <nav className="fixed top-0 left-0 right-0 z-50  shadow bg-white border-gray-200 dark:bg-gray-900">
//         <div className="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto mr-3 p-2">
//           <a href="/" className="flex items-center">
//             <img
//               src= {Logo}
//               className="h-14 "
//               alt="Dreamjob Logo"
//             />
//           </a>
//           <button
//             data-collapse-toggle="navbar-default"
//             type="button"
//             className="inline-flex items-center p-2 ml-3 text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
//             aria-controls="navbar-default"
//             aria-expanded="false"
//           >
//             <span className="sr-only">Open main menu</span>
//             <svg
//               className="w-6 h-6"
//               aria-hidden="true"
//               fill="currentColor"
//               viewBox="0 0 20 20"
//               xmlns="http://www.w3.org/2000/svg"
//             >
//               <path
//                 fillRule="evenodd"
//                 d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
//                 clipRule="evenodd"
//               />
//             </svg>
//           </button>
          // <div className="hidden w-full md:block md:w-auto" id="navbar-default">
          //   <ul className="font-medium flex flex-col p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700">
          //     <li>
          //       <a
          //         href="/"
          //         className="block py-2 pl-3 pr-4 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
          //       >
          //         Home
          //       </a>
          //     </li>
          //     <li>
          //       <a
          //         href="/#vacancy"
          //         className="block py-2 pl-3 pr-4 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
          //       >
          //         Vacancy
          //       </a>
          //     </li>
          //     <li>
          //       <a
          //         href="#contact"
          //         className="block py-2 pl-3 pr-4 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
          //       >
          //         Contact
          //       </a>
          //     </li>
          //   </ul>
          // </div>
//         </div>
//       </nav>
//     </>
//   );
// };

// export default Navbar;
