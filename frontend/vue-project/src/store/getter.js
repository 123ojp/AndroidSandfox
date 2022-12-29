export const getIsLogin = state => { 
    if (state.login_info ){
        return state.login_info.islogin
    }
    return false
}
export const getLoginUsername = state => { 
    if (state.login_info ){
        return state.login_info.username
    }
    return null
}
export const getLoginEmail = state => { 
    if (state.login_info ){
        return state.login_info.email
    }
    return null
}
export const getLoginID = state => { 
    if (state.login_info ){
        return state.login_info.id
    }
    return null
}
