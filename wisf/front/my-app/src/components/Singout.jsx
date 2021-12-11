import SignoutSuccess from './SignoutSuccess';
import { useNavigate } from 'react-router-dom';

export default function Signout(){
    const navigate = useNavigate();

    function getCookie(name){
        let cookieValue = null;
        if (document.cookie && document.cookie !== ''){
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++){
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')){
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const csrftoken = getCookie('csrftoken');

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