import React, {useState, useEffect} from 'react';
import ReactDOM from 'react-dom';

const API_ENDPOINT = process.env.REACT_APP_API_ENDPOINT


const Navbar = () => {
    const [userName, setUserName] = useState(null);

    useEffect(() => {

    })

    return (
        <ul>
            {userName
                ?
                <div>
                    <li><span>{userName}</span></li>
                    <li><a href="/auth/logout">Log out</a> </li>
                </div>
                :
                <div>
                    <li><a href="/auth/register">Register</a></li>
                    <li><a href="/auth/login">Log In</a></li>
                </div>
            }
        </ul>
    )
}

ReactDOM.render(
    <React.StrictMode>
        <Navbar />
    </React.StrictMode>,
    document.getElementById('nav-bar')
);


ReactDOM.render(
    <React.StrictMode>
    </React.StrictMode>,
    document.getElementById('content')
);
