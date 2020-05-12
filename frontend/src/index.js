import React, {useState, useEffect} from 'react';
import { Link } from 'react-router-dom';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import ReactDOM from 'react-dom';

import Navbar from "./navbar"; import './navbar'

const API_ENDPOINT = process.env.REACT_APP_API_ENDPOINT

const Register = () => {
    return (
        <div>
            <header><h1>Register</h1></header>
            <form method="post">
                <label htmlFor="username">Username</label>
                <input name="username" id="username" required/>
                <label htmlFor="password">Password</label>
                <input type="password" name="password" id="password" required/>
                <input type="submit" value="Register"/>
            </form>
        </div>
    );
}

const Index = () => {
    return (
        <div>
            <header><h1>Posts</h1></header>
        </div>
    );
}


ReactDOM.render(
    <React.StrictMode>
        <Router>
            <Navbar />
            <section className="content">
                <Route exact path="/" component={Index}/>
                <Route path="/register" component={Register}/>
            </section>
        </Router>
    </React.StrictMode>,
    document.getElementById('content')
);
