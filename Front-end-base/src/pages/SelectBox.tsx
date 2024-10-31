import { Input } from "../components";
// import { useState } from "react";
const Select = ({isClicked, ifClicked}: {isClicked:boolean; ifClicked:boolean}) => {
  //  const [isEnabled, setIsEnabled] = useState(true);

  const clicked = () => {
    // ifClicked = ;
    if (isClicked === true) {
        ifClicked = true;
    }else {
        ifClicked = false;
    }

    return ifClicked;
  };
  return (
    <div className="border-[2px] space-y-4 h-[40vh] border-dashed border-slate-400 bg-slate-100 flex flex-col items-center justify-center py-4">
      <label
        htmlFor="file-upload"
        className="cursor-pointer bg-blue-800 text-white px-14 py-3 text-xl font-semibold"
        onClick={clicked}
      >
        <i className="fa-solid fa-file-arrow-up mr-1"></i> Select
      </label>
      <Input type="file" classes="hidden" id={"file-upload"} />

      <p className="text-slate-400 italic">max 250mb</p>
    </div>
  );
};

export default Select;
