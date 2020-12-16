import React from 'react';
import {Button } from 'react-bootstrap';
export default function workers_management() {
  return (
  <div >
    <Button variant="dark" style={styles.move} >List Of Workers</Button>
    <Button variant="danger">Add New Worker</Button>
  </div>

  );
}

const styles =({

  move:{
    marginLeft:500


  }
  ,
  title: {
    
  }
});
