import { createSlice, createEntityAdapter, PayloadAction, EntityState } from '@reduxjs/toolkit';
import { RootState } from '../../app/store';

export interface Workspace {
    id: number;
    name: string;
    isActive: boolean;
};

export interface WorkspacesState extends EntityState<Workspace> {
    active: number;
};

const workspacesAdapter = createEntityAdapter<Workspace>();

const initialState: WorkspacesState = workspacesAdapter.getInitialState({
    active: 0,
});

export const workspaceSlice = createSlice({
    name: "workspaces",
    initialState,
    reducers: {
        workspaceAdded(state, action: PayloadAction<Workspace>) {
            workspacesAdapter.addOne(state, action.payload);
            state.active = action.payload.id;
        },
        workspaceRemoved(state, action: PayloadAction<number>) {
            workspacesAdapter.removeOne(state, action.payload);
            state.active = Number(state.ids[0]);
        },
        workspaceSelected(state, action: PayloadAction<number>) {
            state.active = action.payload
        },
    },
});

export const {
    selectIds: selectWorkspaceIds,
    selectAll: selectWorkspaces,
    selectById: selectWorkspaceById,
    selectTotal: selectNumWorkspaces,
    selectEntities: selectWorkspaceEntities,
} = workspacesAdapter.getSelectors<RootState>(state => state.workspaces);

export const selectActiveWorkspaceId = (state: RootState) => state.workspaces.active;

export const {
    workspaceAdded,
    workspaceRemoved,
    workspaceSelected,
} = workspaceSlice.actions;

export default workspaceSlice.reducer;
