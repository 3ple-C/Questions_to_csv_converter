import { Link, SvgNav } from "../components";


const Navbar = () => {
  return (
    <nav className="flex items-center justify-between px-10 h-16 bg-slate-100">
      <SvgNav />
      <Link text={'Recent Files'} className="text-black flex items-center text-xl pb-1 hover:bg-slate-50 h-full"/>
    </nav>
  );
};

export default Navbar;
