import { configureStore, ThunkAction, Action } from '@reduxjs/toolkit';
import userReducer from '../features/user/userSlice';
import counterReducer from '../features/counter/counterSlice';
import workspacesReducer from '../features/workspaces/workspacesSlice';

export const store = configureStore({
  reducer: {
    counter: counterReducer,
    workspaces: workspacesReducer,
    user: userReducer,
  },
});

export type AppDispatch = typeof store.dispatch;
export type RootState = ReturnType<typeof store.getState>;
export type AppThunk<ReturnType = void> = ThunkAction<
  ReturnType,
  RootState,
  unknown,
  Action<string>
>;
