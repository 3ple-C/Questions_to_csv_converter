// import { Button } from "../components";
// import { useState } from "react";


const Content = ({ ifClicked }: {ifClicked:boolean}) => {
    //  const [isEnabled, setIsEnabled] = useState(true);

    //  const toggleButton = () => {
       
    //  }
  return (
    <>
      <section className="flex">
        <div className="space-y-2 w-1/2">
          {/* <Button
            text={"Convert" }
            classes={}
          /> */}

          <button
            disabled={ifClicked === false  ? true : false}
            className={`bg-green-500 font-semibold text-white text-xl py-3 px-14 `}
            id="btn"
          >
            Convert <i className="fa-solid fa-arrow-right ps-1"></i>
          </button>
        </div>
        <div className="space-y-2 w-1/2">
          <h3>
            With this online tool you can easily convert .docx files to CSV. All
            you have to do is upload your file here in the browser and then
            convert the .docx file to CSV.
          </h3>
          <h4>How to convert Markdown to PDF</h4>
          <ul className="space-y-1">
            <li>
              {" "}
              <i className="fa-solid fa-check-double pr-2"></i>
              Choose or drop the Docx file you would like to convert to CSV
            </li>
            <li>
              {" "}
              <i className="fa-solid fa-check-double pr-2"></i>
              Click on 'Convert' below After a few seconds you can download your
              converted CSV file(s)
            </li>
          </ul>
        </div>
      </section>
    </>
  );
};

export default Content;
