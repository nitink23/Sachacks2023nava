import React from 'react'

const JobCard = ({job}) => {


  return (
    <div className='max-w-1/3 p-2 border-2 rounded-lg'>
        <h1 className='text-center p-2 text-[36px]'>Data Science Internship post</h1>
        <a href="https://www.indeed.com/jobs?q=data+science+internship&start=10&pp=gQAPAAAAAAAAAAAAAAACFjYwFgAqAQAIDFMgD47VicQURTW-ZUJIZrthttvaMCLtRBQOn_rmv9LcmsXZyBscAAA&vjk=7e13a0aa1e1a9b29"><h2 className='text-center p-2 text-[24px] text-blue-200 underline'>Check it out on Indeed</h2></a>
        <h3 className='text-center p-2'>73% Match</h3>

    </div>
  )
}

export default JobCard