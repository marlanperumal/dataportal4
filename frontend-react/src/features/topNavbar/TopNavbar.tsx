import React, { useState } from 'react';
import { Navbar, NavbarBrand, Nav, NavItem, NavLink, Dropdown, DropdownToggle, DropdownMenu, DropdownItem } from 'reactstrap';
import eighty20Logo from '../../assets/img/eighty20.png';
import { FaSearch, FaBell, FaQuestionCircle, FaUser } from 'react-icons/fa';

function TopNavbar() {
    const [dropdownOpen, setDropdownOpen] = useState(false);
    return (
        <Navbar color="dark" dark>
            <img src={eighty20Logo} alt="Logo" height={40}/>
            <NavbarBrand href="/" className="mx-2 h1 mb-0">
                DATAPORTAL
            </NavbarBrand>
            <Nav navbar className="me-auto">
                <NavItem><NavLink>| Eighty20</NavLink></NavItem>
            </Nav>
            <FaSearch className="mx-2 text-light"/>
            <FaQuestionCircle className="mx-2 text-light"/>
            <FaBell className="mx-2 text-light"/>
            <Nav className="text-light">
                <Dropdown isOpen={dropdownOpen} nav toggle={() => setDropdownOpen(!dropdownOpen)}>
                    <DropdownToggle caret nav>
                        <FaUser className="text-light"/>
                    </DropdownToggle>
                    <DropdownMenu>
                        <DropdownItem header>Marlan Perumal</DropdownItem>
                        <DropdownItem divider/>
                        <DropdownItem>Admin</DropdownItem>
                        <DropdownItem>Edit Profile</DropdownItem>
                        <DropdownItem href="/login">Logout</DropdownItem>
                    </DropdownMenu>
                </Dropdown>
            </Nav>
        </Navbar>
    );
}

export default TopNavbar;
