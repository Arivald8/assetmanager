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
                localStorage.removeItem('user_email')
                localStorage.removeItem('user_id')
                navigate('/signin')
                navigate(0)
            }
            else{
                console.log(data)
            }
        });
    }

    logout()

    return null;
}