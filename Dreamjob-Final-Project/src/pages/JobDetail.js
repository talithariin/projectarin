import React, { useContext, useEffect, useState } from "react";
import { GlobalContext } from "../context/GlobalContext";
import { useParams } from "react-router-dom";
import JobVacancy from "./JobVacancy";

const JobDetail = () => {
    const { id } = useParams()
    const { data, fetchStatus, setFetchStatus, functions } = useContext(GlobalContext)
    const { fetchData , handleText, handleStatus, handleRupiah } = functions

    const [jobData, setJobData ] = useState(null)

    useEffect(() => {
        if(fetchStatus) {
            fetchData()
            setFetchStatus(false)
        }

        // Cari data pekerjaan berdasarkan ID
        const job = data.find((res) => res.id === parseInt(id));

        setJobData(job)
    }, [fetchStatus, setFetchStatus, fetchData, data, id])
        
    if(!jobData){
        return <h1>Data pekerjaan tidak ditemukan.</h1>
    }

    return (
        <>
            <div className="pt-28 pb-20 bg-pink-100">
                <div class="items-center flex flex-col w-3/4 gap-5 p-5 m-auto bg-white shadow-lg sm:p-4 sm:h-fit rounded-2xl sm:flex-row ">
                    <img 
                        src={jobData.company_image_url}
                        className="object-contain w-full h-52 sm:h-full sm:w-72 rounded-xl"
                        alt="Logo Company"
                    />            
                <div class="flex flex-col flex-1 gap-2">
                    <div class="flex flex-col flex-1 my-1">
                        <div class="w-full h-fit">
                            <h5 className="text-4xl font-bold text-pink-700">
                                <p>
                                    {jobData.title}
                                </p>
                            </h5>
                        </div>
                        <div class="my-1 w-full h-fit bg-transparent">
                            <p className="text-lg font-bold tracking-tight text-gray-900">
                                {jobData.company_name}
                                <div className="ml-5 font-normal w-fit border border-none badge bg-[#87CED0] text-white badge-primary">
                                    {handleStatus(jobData.job_status)}
                                </div>
                            </p>
                        </div>
                        <div class="my-2 w-full h-fit rounded-2xl">
                            <p className="text-base font-normal text-gray-900">
                                <b>Location    :    </b>{jobData.company_city}
                            </p>

                            <p className="text-base font-normal text-gray-900 text-justify">
                                <b>Description :    </b>{jobData.job_description}
                            </p>
                            <p className="text-base font-normal text-gray-900 text-justify">
                                <b>Qualification :    </b>{jobData.job_qualification}
                            </p>
                            <p className="text-base font-normal text-gray-900 text-justify">
                                <b>Salary :    </b>{handleRupiah(jobData.salary_min)} - {handleRupiah(jobData.salary_max)}
                            </p>
                        </div>
                    </div>
                    <div class="flex gap-3">
                        <div className="font-normal w-fit border border-none badge bg-[#F4A2D0] text-white badge-primary">
                            {jobData.job_tenure}
                        </div>
                        <div className="font-normal w-fit border border-none badge bg-[#F4A2D0] text-white badge-secondary">
                            {jobData.job_type}
                        </div>
                    </div>
                </div>
            </div>
            </div>
            <div>
                <JobVacancy/>
            </div>
        </>

    );
};

export default JobDetail;