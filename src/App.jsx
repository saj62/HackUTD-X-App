import { useState } from 'react'
import './App.css'
//import { Login } from "./pages/Login"
//import { Register } from "./pages/Register"
import WelcomePage from './components/WelcomePage'

// This is the file that runs.
function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="App">
      <Login />
    </div>
  )
}

export default App
