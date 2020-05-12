import React, {useContext, useState, useEffect} from 'react';
import { Link } from 'react-router-dom';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import ReactDOM from 'react-dom';

import Navbar from "./navbar"; import './navbar'

const API_ENDPOINT = process.env.REACT_APP_API_ENDPOINT
const HeaderContext = React.createContext(["Posts", () => {}]);

const Register = () => {
    const [headerName, setHeaderName] = useContext(HeaderContext);
    useEffect(() => {
        setHeaderName("Register");
    });

    return (
        <form method="post">
            <label htmlFor="username">Username</label>
            <input name="username" id="username" required/>
            <label htmlFor="password">Password</label>
            <input type="password" name="password" id="password" required/>
            <input type="submit" value="Register"/>
        </form>
    );
}

const Index = () => {
    const [headerName, setHeaderName] = useContext(HeaderContext);

    useEffect(() => {
        setHeaderName("Posts");
    });

    return (
        <div></div>
    );
}

const Section = () => {
    const [headerValue, setHeaderValue] = useState("Posts");
    return (
        <section className="content">
            <header><h1>{headerValue}</h1></header>
            <HeaderContext.Provider value={[headerValue, setHeaderValue]}>
                <Route exact path="/" component={Index}/>
                <Route path="/register" component={Register}/>
            </HeaderContext.Provider>
        </section>
    );
}


ReactDOM.render(
    <React.StrictMode>
        <Router>
            <Navbar />
            <Section/>
        </Router>
    </React.StrictMode>,
    document.getElementById('content')
);
