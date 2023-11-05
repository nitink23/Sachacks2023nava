'use client'

import JobCard from "@/components/JobCard";
import NavBar from "@/components/NavBar";
import UploadComponent from "@/components/UploadComponent";
import { useState, useEffect } from "react";
import { ChevronsDown } from 'lucide-react';


export default function Home() {
  const [resultsActive, setResultsActive] = useState(
    {
      count:0,
      active:false
    })


  useEffect(() => {
    if (resultsActive.active) {
      // Scroll to the results section when resultsActive becomes true
      document.getElementById("results").scrollIntoView({ behavior: "smooth" });

    }
  }, [resultsActive]);


  return (
    <div className="flex flex-col overflow-x-hidden">
      <div className="flex flex-grow min-h-screen flex-col items-center px-24 pb-24">
        <NavBar />
        <UploadComponent setActive={setResultsActive} active={resultsActive} />
      </div>
      {resultsActive.active &&
        <a className="self-center absolute bottom-0 hover:cursor-pointer">
          <ChevronsDown color="rgb(59 130 246)" size={100} className="" onClick={()=>{
            document.getElementById("results").scrollIntoView({ behavior: "smooth" });
          }} />
        </a>
      }
      { resultsActive.active &&
        <section id="results" className="flex min-h-screen flex-col items-center px-24 pb-24">
          <h1 className=" font-bold font-mono text-blue-500 text-[76px] text-center mt-5">Here's What We Found!</h1>
          <div className="flex gap-5 mt-10">
            <JobCard />
            <JobCard />
            <JobCard />
          </div>
        </section>
      }
    </div>
  )
}
