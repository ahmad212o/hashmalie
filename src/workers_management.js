import React,{useState} from 'react';
import {Button } from 'react-bootstrap';

function Clicks() {
  const[count,setCount]=useState(0);
  const[clicked,setClicked]=useState(false);

  return (
  <div id ="root">
    <Button variant={clicked? "success" : "dark"}onClick={test2} style={styles.move}  >List Of Workers</Button>
    <Button variant="danger" onClick={test}>Add New Worker</Button>

  <div id="portal"></div>
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
