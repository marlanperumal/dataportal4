import "../styles/Header.css";

function Header({ screen, user }) {
  function handleNavigationClick(url) {}

  function openHelp() {
    console.log("Open Help");
  }

  const loginmsg = user ? (
    <li>
      <span className="message">Welcome back {user.name} </span>
    </li>
  ) : (
    <li>
      <span className="message" />
    </li>
  );

  const login = !user && (
    <li>
      <a href="/login/">
        <i className="fa fa-user" />
        Login
      </a>
    </li>
  );

  const signup = !user && (
    <li>
      <a href="/signup/">
        <i className="fa fa-edit" />
        Sign Up
      </a>
    </li>
  );

  const admin = user?.is_admin && (
    <li>
      <i className="fa fa-cogs" />
      <a onClick={() => handleNavigationClick("/admin")}>Admin</a>
    </li>
  );

  const userNav = user && (
    <li className="dropdown">
      <a
        href="#"
        className="dropdown-toggle"
        data-toggle="dropdown"
        role="button"
        aria-haspopup="true"
        aria-expanded="false"
      >
        <i className="fa fa-user" />
        Account
        <span className="caret" />
      </a>
      <ul className="dropdown-menu">
        {admin}
        <li>
          <i className="fa fa-list-alt" />
          <a onClick={() => handleNavigationClick("/")}>My Workspaces</a>
        </li>
        <li>
          <i className="fa fa-cog" />
          <a onClick={() => handleNavigationClick("/user_account")}>
            Account Settings
          </a>
        </li>
        <li>
          <i className="fa fa-sign-out" />
          <a onClick={() => handleNavigationClick("/logout/")}>Logout</a>
        </li>
      </ul>
    </li>
  );

  return (
    <div className="navbar navbar-default" role="navigation">
      <div className="container-fluid">
        <div className="navbar-header">
          <button
            type="button"
            className="navbar-toggle collapsed"
            data-toggle="collapse"
            data-target="#application_menu"
            aria-expanded="false"
          >
            <span className="sr-only" />
            <span className="icon-bar" />
            <span className="icon-bar" />
            <span className="icon-bar" />
          </button>
          <a className="navbar-brand" href="/home" />
        </div>

        <div
          className="collapse navbar-collapse header-navigation-options"
          id="application_menu"
        >
          <ul className="nav navbar-nav navbar-right text-center">
            {loginmsg}
            {signup}
            {login}
            {userNav}
            <li>
              <a onClick={() => handleNavigationClick.bind("/pricing")}>
                <i className="fa fa-cubes" />
                Packages
              </a>
            </li>
            <li>
              <a onClick={openHelp}>
                <i className="fa fa-question-circle" aria-hidden="true" />
                Help
              </a>
            </li>
            <li>
              <a
                onClick={() =>
                  handleNavigationClick.bind("https://www.eighty20.co.za")
                }
              >
                <i className="fa fa-home" />
                Eighty20
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
}

export default Header;
