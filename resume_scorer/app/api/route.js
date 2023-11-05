import { connectMongoDB } from "@/lib/mongo";
import S3 from "aws-sdk/clients/s3";
import { NextResponse } from "next/server";
import { PassThrough } from "stream";

const s3 = new S3({
  apiVersion: "2006-03-01",
  accessKeyId: process.env.ACCESS_KEY,
  secretAccessKey: process.env.SECRET_KEY,
  region: process.env.REGION,
  signatureVersion: "v4",
});

export async function POST(request) {
    const { key } = await request.json();
  
    const params = {
      Bucket: process.env.BUCKET_NAME,
      Key: key,
    };
  
    try {
      //@ts-ignore
      await s3.headObject(params).promise();
  
      const downloadStream = new PassThrough();
  
      // @ts-ignore
      await s3.getObject(params).createReadStream().pipe(downloadStream);

      const content = await new Promise((resolve, reject) => {
        let data = "";
        downloadStream.on("data", (chunk) => {
          data += chunk.toString();
        });
        downloadStream.on("end", () => {
          resolve(data);
        });
        downloadStream.on("error", (error) => {
          reject(error);
        });
      });
  
      return NextResponse.json({
          error: false,
          value: content
      });
      // //@ts-ignore
      // return new Response(downloadStream, {
      //   headers: {
      //     "Content-Type": "application/octet-stream",
      //     "Content-Disposition": `attachment; filename="${key}"`,
      //   },
      // });
    } catch (error) {
      if (error.code === "NotFound") {
        // Object does not exist, return an error response
        return NextResponse.json({
          error: true,
          value: `The specified key '${key}' does not exist.`,
        });
      }
      console.log(error)
      return NextResponse.json({
        error: true,
        value: "getObject().promise did not work",
      });
    }
  }