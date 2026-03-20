import { useState, useEffect } from 'react'

function App() {
  const [animalString, setAnimalString] = useState("Figuring it out...")
  const [content, setContent] = useState("")

  useEffect(() => {
    fetch('/api/backToFrontTest')
      .then(res => res.json())
      .then(data => {
        setAnimalString(data.modelResult);
      });
  }, []); // the second argument, the empty list, is important to prevent recursive looping

  

  
  return (
    <div className="App">
      <h1>Please please please work!!</h1>
      <p>String from Backend: {animalString.toLocaleString()}</p>

      <form>
        <input 
          type="text" 
          onChange={e => setContent(e.target.value)} 
        />
        <button 
          type="submit"
          onClick={async (e) => {
            e.preventDefault();
            const dataForBackend = {content}
            try {
              const response = await fetch('/api/frontToBackTest', {
                method: 'POST',
                headers: {
                  'Content-Type': 'application/json',
                },
                body: JSON.stringify(dataForBackend),
              });
            
              const data = await response.json();
              console.log(data);
            } catch (error) {
              console.error('Error connecting to backend:', error);
            }
          }}
        > Send to Flask </button> 
      </form>
    </div>
  );
}

export default App;