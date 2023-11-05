import mongoose from "mongoose";

const URI = "mongodb+srv://nava:sachacks23@cluster0.wdsjs4p.mongodb.net" || "mongodb://127.0.0.1:27017/peide";

if (!URI) throw new Error("Please add your MongoURI to .env");

//CONNECT DB FUNCTION
export const connectMongoDB = async () => {
  try {
    await mongoose.connect(URI);
  } catch (error) {
    console.error(error);
  }
};
