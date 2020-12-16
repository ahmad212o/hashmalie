import React, { useState } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import {Route,BrowserRouter as Router,Switch,Link} from "react-router-dom"
import company_details from "./company_details";
import about from "./About";
import workers_management from "./workers_management"
import Login from "./login"
import pdf from "./pdf_test"
import schedule from "./schedule"
import finance from "./finance"
import projects from "./projects"



export default function app() {
  
  return (
  
<Router>
    
       <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        
  <a class="navbar-brand" href="#">hashmali</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNavDropdown">
    <ul class="navbar-nav">
        <li class="nav-item">
      <Link to="/login" class="nav-link" >Login</Link>
      </li>


      <li class="nav-item active">
      <Link to="/" class="nav-link" >My Company<span class="sr-only">(current)</span></Link>
      </li>
      <li class="nav-item">
      <Link to="/workers_management" class="nav-link" >Workers Management</Link>
      </li>
      <li class="nav-item">
      <Link to="/schedule" class="nav-link" >Schedule</Link>
      </li>
      <li class="nav-item">
      <Link to="/finance" class="nav-link" >Finance</Link>
      </li>
      <li class="nav-item">
      <Link to="/projects" class="nav-link" >Projects</Link>
      </li>
      <li class="nav-item">
      <Link to="/about" class="nav-link" >about</Link>
      </li>

  






    </ul>
  </div>

</nav>

    <Switch>
      <Route>
        <Route path="/"exact component={company_details}/>
        <Route path="/workers_management" component={workers_management}/>
        <Route path="/about" component={about}/>
        <Route path="/login" component={Login}/>
        <Route path="/PDF" component={pdf}/>
        <Route path="/schedule" component={schedule}/>
        <Route path="/finance" component={finance}/>
        <Route path="/projects" component={projects}/>

        
      </Route>
    </Switch>
    </Router>
  );
}
