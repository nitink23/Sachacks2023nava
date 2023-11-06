'use client'

import React, { useState } from 'react';
import { Upload } from 'lucide-react';
import AWS from 'aws-sdk';

const s3 = new AWS.S3({
  accessKeyId: process.env.ACCESS_KEY,
  secretAccessKey: process.env.SECRET_KEY,
  region: process.env.REGION,
});

const UploadComponent = ({setActive, active}) => {

  const [filename, setFilename] = useState("")

  
  const handleMatching = async () =>{
    console.log("Running")
    const pdf_response = await fetch(`api/`, {
        method: "POST",
        headers: {
            "Content-Type":"application/json"
        },
        body: JSON.stringify({
            key: filename
        })
    })

    if (pdf_response.ok) {
        const data = await pdf_response.json();
        if(!data.error){
          extractTextFromPDF(data.value)
        }
        console.log("PDF DATA", data)
    }
  }

  const handleFileUpload = async (event) => {
    const file = event.target.files[0];

    // console.log("FILE", file)
    
    if (!file) return;
    
    console.log("BUCKETS", process.env.BUCKET_NAME)
    
    try {
        const params = {
            Bucket: "resource-scorer",
            Key: file.name,
            Body: file,
        };
        
        await s3.upload(params).promise();
        setFilename(file.name)
        setActive({
            count: active+1,
            active: true
        })
        handleMatching();
    } catch (error) {
      console.error('Error uploading file to S3:', error);
    }
  };

  return (
    <div className='flex flex-col justify-center items-center'>
        <h1 className='font-bold font-mono text-[30px] text-blue-500 mb-2'>{filename? filename : null }</h1>
        <label className="w-[25vw] h-[25vw] flex items-center justify-center rounded-full bg-blue-500 hover:cursor-pointer">
        <input
            type="file"
            accept=".pdf"
            style={{ display: 'none' }}
            onChange={handleFileUpload}
        />
        <Upload size={200} color="white" />
        </label>
    </div>
  );
};

export default UploadComponent;
