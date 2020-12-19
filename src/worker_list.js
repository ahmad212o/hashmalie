import React from 'react';

function Worker(){
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
        <li key={data.id}> {data.name} {data.name}</li>

      ))}
    </ul>
);


}

export default Worker;









const styles =({

  move:{
    marginLeft:500


  }
  ,
  title: {
    
  }
});
