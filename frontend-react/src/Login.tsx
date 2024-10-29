import React from 'react';
import { Button, Form, FormGroup, Input, Label } from 'reactstrap';
import { Link, useNavigate } from 'react-router-dom';

import eighty20Logo from './assets/img/eighty20.png';

function Login() {
    const navigate = useNavigate();
    function onSubmit(e: React.FormEvent) {
        e.preventDefault();
        const target = e.target as typeof e.target & {
            email: { value: string };
            password: { value: string };
          };
        const email = target.email.value;
        const password = target.password.value;
        console.log(email, password);
        navigate("/")
    }

    return (
        <div className="text-center d-flex align-items-center justify-content-center bg-dark h-100" style={{"minHeight": "100vh"}}>
                <Form className="w-25" onSubmit={onSubmit}>
                    <img src={eighty20Logo} alt="Logo"/>
                    <h3 className="text-light">DATAPORTAL</h3>
                    <div className="text-light mb-2">Please sign in</div>
                    <FormGroup floating>
                        <Input id="email" placeholder="Email" type="email"/>
                        <Label for="email">Email</Label>
                    </FormGroup>
                    <FormGroup floating>
                        <Input id="password" placeholder="Password" type="password"/>
                        <Label for="password">Password</Label>
                    </FormGroup>
                    <Button>Login</Button>
                    <div className="mt-3 text-light">
                        <Link to="/resetPasswordRequest">Forgot Password?</Link>
                        {" | "}
                        <Link to="/register">Register</Link>

                    </div>
                </Form>
        </div>
    );
}

export default Login;
