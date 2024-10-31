import './App.css'
import {Content, Header,Navbar, Select} from './pages';
import { Main } from './pages/_components';

import { useState } from "react";




function App() {
  const [isClicked, ifClicked] = useState(true);
  const buttonToggle = () => ifClicked((state) => !state);

  return (
    <>
      <Navbar />

      <Main>
        <Header />
        <Select />
        <Content />
      </Main>
    </>
  );
}

export default App
