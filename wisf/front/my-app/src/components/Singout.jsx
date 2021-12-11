import { useNavigate } from 'react-router-dom';
import { csrftoken } from './ApiCaller';

export default function Signout(){
    const navigate = useNavigate();

    let logout = () => {
        const request = new Request(
            'http://127.0.0.1:8000/logout/',
            {
                headers: {'X-CSRFToken': csrftoken},
                method: 'POST',
                mode: 'cors',
                credentials: 'include',
            }
        );

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
    }

    logout()

    return null;
}