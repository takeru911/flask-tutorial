import React, {useState, useEffect} from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
    const [userName, setUserName] = useState(null);

    useEffect(() => {

    })

    return (
        <div id="nav-bar">
            <nav>
                <h1>Flaskr</h1>
                <ul>
                    {userName
                        ?
                        <div>
                            <li><span>{userName}</span></li>
                            <li><Link to="/logout">Log out</Link> </li>
                        </div>
                        :
                        <div>
                            <li><Link to="/register">Register</Link></li>
                            <li><Link to="/login">Log In</Link></li>
                        </div>
                    }
                </ul>
            </nav>
        </div>
    )
}

export default Navbar