import { useNavigate } from 'react-router-dom';
import { makeRequest } from './ApiCaller';

export default function Signout(){
    const navigate = useNavigate();
    let request = makeRequest(null, "logout")

    fetch(request).then(function(response){
        return response.json()
    }).then(function(data){
        if (data['Success']){
            localStorage.removeItem('user_id')
            localStorage.removeItem('user_email')
            navigate('/signin')
            navigate(0)
            alert("You have been successfully signed out.")
        }
        else{
            alert('We were unable to sign you out at this time. Please try again.')
        }
    });

    return null;
}