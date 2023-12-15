import axios from "axios"
import React, { createContext, useState } from "react"
import { useNavigate, useParams } from "react-router-dom"

export const GlobalContext = createContext()

export const GlobalProvider = props => {
    let navigate = useNavigate()
    const [data, setData] = useState([])
    const [fetchStatus, setFetchStatus] = useState(true)
    const [searchStatus, setSearchStatus] = useState(true)
    const [currentId, setCurrentId] = useState(null)
    const [input, setInput] = useState({
        title: "",
        job_description: "",
        job_qualification: "",
        job_type: "",
        job_tenure: "",
        job_status: true,
        company_name: "",
        company_image_url: "",
        company_city: "",
        salary_max: 0,
        salary_min: 0,
    })

    const fetchData = async () => {
        let result = await axios.get(`https://dev-example.sanbercloud.com/api/job-vacancy`)
        let fetchResult = result.data.data
        console.log(fetchResult)
        setData(
            fetchResult.map((res) => {
                return {
                    id : res.id,
                    title : res.title,
                    job_description : res.job_description,
                    job_qualification : res.job_qualification,
                    job_type : res.job_type,
                    job_tenure : res.job_tenure,
                    job_status : res.job_status,
                    company_name : res.company_name,
                    company_image_url : res.company_image_url,
                    company_city : res.company_city,
                    salary_min : res.salary_min,
                    salary_max : res.salary_max
                }

            })
        )
    }

    const handleRupiah = (angka) => {
        if (angka !== null) {
          var number_string = angka.toString(),
            split = number_string.split(","),
            sisa = split[0].length % 3,
            rupiah = split[0].substr(0, sisa),
            ribuan = split[0].substr(sisa).match(/\d{3}/gi),
            separator;
      
          // tambahkan titik jika yang di input sudah menjadi angka ribuan atau jutaan
          if (ribuan) {
            separator = sisa ? "." : "";
            rupiah += separator + ribuan.join(".");
          }
      
          rupiah = split[1] !== undefined ? rupiah + "," + split[1] : rupiah;
      
          // Mengecek jika angka lebih besar atau sama dengan 1 miliar (miliaran)
          if (angka >= 1000000000) {
            return "Rp" + Math.round(angka / 1000000000) + " M";
          }
          
          // Mengecek jika angka lebih besar atau sama dengan 1 juta (jutaan)
          if (angka >= 1000000) {
            return "Rp" + Math.round(angka / 1000000) + " juta";
          }
          
          // Mengecek jika angka lebih besar atau sama dengan 100 ribu
          if (angka >= 1000) {
            return "Rp" + Math.round(angka / 1000) + " rb";
          }
      
          return rupiah === "0" ? "Free" : "Rp" + parseInt(rupiah).toString();
        } else {
          return "Free";
        }
      }
      
    const handleStatus = (params) =>{
        if(params === undefined){
            return ""
        }
        else if (params === 1){
            return "Available"
        }
        else if (params === 0){
            return "Closed"
        }

    }

    const handleText = (params, max) => {
        if (params === null || params === undefined) {
            return "";
        } else if (params.length <= max) {
            return params;
        } else {
            return params.slice(0, max) + "...";
        }
    }    

    const functions = {
        fetchData,
        handleText,
        handleStatus,
        handleRupiah
    }

    return (
        <GlobalContext.Provider value={{
            data,
            setData,
            fetchStatus,
            setFetchStatus,
            searchStatus, 
            setSearchStatus,
            currentId,
            setCurrentId,
            input,
            setInput,
            functions
        }}>
            {props.children}
        </GlobalContext.Provider>
    )


}