import React, { useContext, useEffect } from "react";
import { GlobalContext } from "../context/GlobalContext";
import Money from "../assets/Money.svg"
import Location from "../assets/Location.svg"
import { Button } from 'flowbite-react';
import { HiOutlineArrowRight, HiShoppingCart } from 'react-icons/hi';
import { Link } from "react-router-dom"

const JobVacancy = () => {
    const { data, fetchStatus, setFetchStatus, functions } = useContext(GlobalContext)
    const { fetchData, handleText, handleStatus, handleRupiah } = functions

    console.log(data);

    useEffect(() => {
        if(fetchStatus) {
            fetchData()
            setFetchStatus(false)
        }
    }, [fetchStatus, setFetchStatus, fetchData])

    return (
        <>
          <section id="vacancy" className="bg-pink-100 items-center justify-center">
            <div className="text-4xl font-bold text-center container mb-10 mt-30 bg-pink-100">
              <h1>Find your Dream Job!</h1>
            </div>
        
            <div className="bg-pink-100 ml-9 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-x-4 gap-y-6 justify-center items-center mb-10">
              {data !== null && data.map((res) => {
                return(
                  <div
                    key={res.id}
                    className="bg-white w-4/5 sm:w-4/5 md:w-5/6 h-fit place-items-center items-center border border-pink-200 rounded-lg drop-shadow-md shadow-md shadow-pink-300">
                      <div className="mb-5">
                        <div className="md:flex font-normal text-xs text-center flex justify-center items-center m-3 pt-5">
                          <div className="w-3/5 border border-none badge bg-[#F4A2D0] text-white badge-primary px-3 py-1 mx-1">{handleStatus(res.job_status)}</div>
                          <div className="w-3/5 border border-none badge bg-[#87CED0] text-white badge-secondary px-3 py-1 mx-1">{res.job_type}</div>
                        </div>

                        <div className="w-3/4 p-1 mx-2">
                          <h5 className= "text-xl font-bold tracking-tight text-black">
                            {res.title}
                          </h5>
                          <p className="mt-1 block w-auto text-sm">
                            {handleText(res.job_description, 20)}                      
                          </p>
                        </div>

                        <div className="flex m-2">
                          <img
                            src={Money}
                            className="h-6 w-6 mx-2"
                            alt="Salary"
                          />
                          <p className="font-netral text-sm">
                            {handleRupiah(res.salary_min)} - {handleRupiah(res.salary_max)}
                          </p>
                        </div>

                        <div className="flex items-center">
                          <img
                            src={`${res.company_image_url}`}
                            class="my-2 ml-4 mr-2 w-1/5 bg-cover bg-landscape"
                            alt="Company Logo"
                          />
                          <div className="flex flex-col ml-0 mr-2">
                            <h2 className="w-full font-medium">{res.company_name}</h2>
                            <div className="flex">
                              <img
                                src={Location}
                                className="h-4 w-4 mr-1 mt-1"
                                alt="Lokasi"
                              />
                              <p className="font-netral text-sm text-gray-600">
                                {res.company_city}
                              </p>
                            </div>
                            
                          </div>  
                                        
                        </div>
                        <Link to={`/job-vacancy/${res.id}`}>
                        <Button size="sm" gradientMonochrome="pink" className="mx-4 bottom-0 top-3">
                            <p>
                              Detail
                            </p>
                            <HiOutlineArrowRight className="ml-2 h-5 w-5"/>
                        </Button>
                      </Link>
                      </div>
                  </div>
                  
    
                  )
              })}
            </div> 
            <div className="bg-pink-100 h-16"></div>
          </section>
        </>
      );
};
    
export default JobVacancy;

