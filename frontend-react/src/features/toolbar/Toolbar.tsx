import * as React from 'react';
import { Navbar, Nav, NavItem, NavLink } from 'reactstrap';

function Toolbar() {
    return (
        <Navbar color="light">
            <Nav>
                <NavItem><NavLink>Toolbar</NavLink></NavItem>
            </Nav>
        </Navbar>
    )
}

export default Toolbar
