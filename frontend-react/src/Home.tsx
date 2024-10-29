import React from 'react';
import { Container, Row, Col } from 'reactstrap';

import TopNavbar from './features/topNavbar/TopNavbar';
import BottomNavbar from './features/bottomNavbar/BottomNavbar';
import Toolbar from './features/toolbar/Toolbar';

function Home() {
    return (
        <div>
            <TopNavbar/>
            <Container fluid className="h-100">
                <Toolbar/>
                <Row className="h-100">
                    <Col className="bg-light h-100" md="3">Field Tree</Col>
                    <Col className="bg-light" md="6">Result</Col>
                    <Col className="bg-light" md="3">Config</Col>
                </Row>
            </Container>
            <BottomNavbar/>
        </div>
    );
}

export default Home;
