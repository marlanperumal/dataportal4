import React, { useState } from 'react';
import { Navbar, Nav, NavItem, NavLink, Dropdown, DropdownToggle, DropdownMenu, DropdownItem } from 'reactstrap';
import { FaBars, FaCopy, FaTimes, FaPen, FaPlus, FaSave, FaShare, FaTrash } from 'react-icons/fa';

import { useAppSelector, useAppDispatch } from '../../app/hooks';
import { selectActiveWorkspaceId, selectWorkspaces, workspaceAdded, workspaceRemoved, workspaceSelected } from '../workspaces/workspacesSlice';

function BottomNavbar() {
    const workspaces = useAppSelector(selectWorkspaces);
    const activeWorkspaceId = useAppSelector(selectActiveWorkspaceId)
    const dispatch = useAppDispatch();
    const [dropdownOpen, setDropdownOpen] = useState(false);

    function addWorkspace() {
        const id = Math.max(0, ...workspaces.map(workspace => Number(workspace.id))) + 1;
        const name = `Workspace ${id}`;
        const isActive = true;
        const workspace = {id, name, isActive}
        dispatch(workspaceAdded(workspace))
    }

    function activateWorkspace(id: number) {
        dispatch(workspaceSelected(id));
    }

    function closeWorkspace(id: number) {
        dispatch(workspaceRemoved(id))
    }

    return (
        <Navbar fixed="bottom" color="light" light>
            <Nav tabs>
                <Dropdown nav isOpen={dropdownOpen} toggle={() => setDropdownOpen(!dropdownOpen)}>
                    <DropdownToggle nav>
                        <FaBars/>
                    </DropdownToggle>
                    <DropdownMenu>
                        <DropdownItem><FaSave/><span className="ps-2">Save</span></DropdownItem>
                        <DropdownItem><FaCopy/><span className="ps-2">Duplicate</span></DropdownItem>
                        <DropdownItem><FaPen/><span className="ps-2">Rename</span></DropdownItem>
                        <DropdownItem><FaShare/><span className="ps-2">Share</span></DropdownItem>
                        <DropdownItem onClick={() => closeWorkspace(activeWorkspaceId)}><FaTimes/><span className="ps-2">Close</span></DropdownItem>
                        <DropdownItem><FaTrash/><span className="ps-2">Delete</span></DropdownItem>
                    </DropdownMenu>
                </Dropdown>
                <NavItem onClick={addWorkspace}><NavLink><FaPlus/></NavLink></NavItem>
                { workspaces.map(workspace =>
                    <NavItem key={workspace.id} onClick={() => activateWorkspace(workspace.id)}>
                        <NavLink active={workspace.id === activeWorkspaceId}
                        >
                            {workspace.name}
                        </NavLink>
                    </NavItem>
                )}
            </Nav>
        </Navbar>
    );
}

export default BottomNavbar;
