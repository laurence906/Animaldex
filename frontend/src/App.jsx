import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom';
import Signup from './pages/signup';
import Login from './pages/login';

// * for fallback page -> WIP, maybe. a real one wouldnt hurt but isnt really necessary.
function App() {
  return (
  <BrowserRouter>
    <Routes>
      <Route path = "/signup" element = {<Signup />} />
      <Route path = "/login" element = {<Login />} />
      <Route path = "*" element = {<Navigate to = "/signup" replace />} /> 
    </Routes>
  </BrowserRouter>
  );
}

export default App