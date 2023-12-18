export const api_host : string = "http://localhost:5000/api/"

export async function login( username : string, password : string) {

    const response = await fetch( api_host + "login", {
     method : 'POST',
     headers :{ 'Content-Type': 'application/json' },
     body : JSON.stringify({username, password}),
     credentials: 'include'
     })
  
    return response
}

export async function logout() {
  const response = await fetch(api_host + 'logout', {
    method: 'POST',
    credentials: 'include' 
})
  return response
}

export async function register(username: string, password: string) {
    const payload = {
      username,
      password,
    };
    const headers = { 'Content-Type': 'application/json' };
  
    const response = await fetch('http://localhost:5000/api/register', {
      method: 'POST',
      headers: headers,
      body: JSON.stringify(payload),
    });
  
    return response
    
  }


export async function check_auth() {
  const response = await fetch(api_host + "check_auth",{
      method: 'GET',
      credentials: 'include'
  })
  if (response.ok) {
    return await response.json()
  } else {
    return null
  }
}
  
export async function get_user_goals(){
    const response = await fetch("http://localhost:5000/api/goals",{
      method: 'GET',
      credentials: 'include'
  })
    const data = await response.json()
  
    return data
  }

export async function set_user_goals( goals : Object) {
  const response = await fetch(api_host + 'goals', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(goals),
      credentials: 'include'
    });
    return response
}
  
export async function get_meal_plan() {
    const response = await fetch("http://localhost:5000/api/meal_plan", {
      method: 'GET',
      credentials: 'include'
  })
  
    const data = await response.json()
    return data
  }