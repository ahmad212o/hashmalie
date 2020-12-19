import React,{useState} from 'react';
import {Button } from 'react-bootstrap';
import Worker from "./worker_list.js"

function Clicks() {
  const[count,setCount]=useState(0);
  const[clicked,setClicked]=useState(false);

  return (
  <div id ="root">
    <Button variant={clicked? "success" : "dark"}onClick={test2} style={styles.move}  >List Of Workers</Button>
    <Button variant="danger" onClick={POST_Register}>Add New Worker</Button>
    <Button variant="danger" onClick={POST_LogIN}>LogINTEEST</Button>

    <Worker/>
      </div>

  );
function print_list(){
console.log("Hello")
  const Movies = [
    { id: 1, name: 'Reservoir Dogs' },
    { id: 2, name: 'Airplane' },
    { id: 3, name: 'Doctor Zhivago' },
    { id: 4, name: 'Memento' },
    { id: 5, name: 'Braveheart' },
    { id: 6, name: 'Beauty and the Beast' },
    { id: 7, name: 'Seven' },
    { id: 8, name: 'The Seven Samurai' }
  ];

  return (
    <ul>
      {Movies.map(data => (
        <li key={data.id}> {data.name}</li>
      ))}
    </ul>
);


}

function generate()
{

}
function test() {
  return <h1>Hello</h1>;
}
function test2() {
     setClicked(!clicked);
    console.log(clicked)
  return <h1>Hello</h1>;
  }
  function GET() {
    // Simple GET request using fetch
    fetch('http://127.0.0.1:8000/api/',{
      method: 'GET', 

    })

    .then(response => response.json())
    .then(data => console.log(data));
}

function POST_Register() {
  // Simple GET request using fetch
  fetch('http://127.0.0.1:8000/api/worker/register/',{
    method: 'POST',headers: { 'Content-Type': 'application/json',
    'Authorization' : 'Token 248ff594940b60bf5a6333afbaa23d41641b22e6 ',
  },
    body: JSON.stringify({ phone: '2000',password:'saed',password2:'saed',
    is_admin:'true',first_name: 'Saed',second_name:'jaber'
  
  })
  })

  .then(response => response.json())
  .then(data => console.log(data));
}

function POST_LogIN() {
  // Simple GET request using fetch
  fetch('http://127.0.0.1:8000/api/worker/login/',{
    method: 'POST',headers: { 'Content-Type': 'application/json',
  
  },
    body: JSON.stringify({ username: '2000',password:'saed' })
  })

  .then(response => response.json())
  .then(data => console.log(data));
}









}
export default Clicks;









const styles =({

  move:{
    marginLeft:500


  }
  ,
  title: {
    
  }
});
