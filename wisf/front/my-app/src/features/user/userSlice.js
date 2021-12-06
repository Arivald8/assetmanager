import { createSlice } from "@reduxjs/toolkit";

export const userSlice = createSlice({
    name: 'user_display',
    initialState: {
        value: "",
    },
    reducers: {
        display_user: (state, user) => {
            state.value = user
        },
        remove_user_display: (state) => {
            state.value = ""
        },
    },
})

export const { display_user, remove_user_display } = userSlice.actions
export default userSlice.reducer