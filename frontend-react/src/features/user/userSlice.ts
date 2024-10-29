import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { RootState } from "../../app/store";

export interface User {
    id?: number;
    firstName?: string;
    lastName?: string;
    email?: string;
    organisationId?: number;
    isAdmin?: boolean;
};

export const userSlice = createSlice({
    name: "user",
    initialState: {},
    reducers: {
        loggedIn(state, action: PayloadAction<User>) {
            state = action.payload;
        }
    }
});

export const selectUser = (state: RootState) => state.user;

export const {
    loggedIn
} = userSlice.actions;

export default userSlice.reducer;
