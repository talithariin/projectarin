import React, { useEffect, useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import JobVacancy from "./pages/JobVacancy";
import JobDetail from "./pages/JobDetail"
import { GlobalProvider } from "./context/GlobalContext";


const App = () => {
  return (
    <>
      <BrowserRouter>
        <GlobalProvider>
          <Navbar />
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/job-vacancy" element={<JobVacancy/>} />
              <Route path="/job-vacancy/:id" element={<JobDetail/>}></Route>
            </Routes>
        </GlobalProvider>
      </BrowserRouter>
    </>
  );
};

export default App;
