import "../styles/Footer.css";

function Footer() {
  const today = new Date();
  const year = today.getFullYear();
  return (
    <div className="footer">
      <div className="footer_Eighty20">
        <div className="footer_links">
          <a
            target="_blank"
            rel="noreferrer"
            href="https://www.eighty20.co.za"
            className="footer_link_item"
          >
            Eighty20 Home
          </a>{" "}
          |
          <a
            target="_blank"
            rel="noreferrer"
            href="https://www.eighty20.co.za/data-services/"
            className="footer_link_item"
          >
            Data Products & Services
          </a>{" "}
          |
          <a
            target="_blank"
            rel="noreferrer"
            href="https://www.eighty20.co.za/consulting/"
            className="footer_link_item"
          >
            Consulting
          </a>{" "}
          |
          <a
            target="_blank"
            rel="noreferrer"
            href="https://www.eighty20.co.za/content-type/reports-presentations/"
            className="footer_link_item"
          >
            See Our Work
          </a>{" "}
          |
          <a
            target="_blank"
            rel="noreferrer"
            href="https://www.eighty20.co.za/about-us/"
            className="footer_link_item"
          >
            About Us
          </a>{" "}
          |
          <a
            target="_blank"
            rel="noreferrer"
            href="https://www.eighty20.co.za/faq-category/general/"
            className="footer_link_item"
          >
            FAQs
          </a>{" "}
          |
          <a
            target="_blank"
            rel="noreferrer"
            href="https://www.eighty20.co.za/contact/"
            className="footer_link_item"
          >
            Contact
          </a>
        </div>
      </div>
      <div className="footer_copyright">
        <span>© Copyright {year} Eighty20. All Rights Reserved.</span>
      </div>
    </div>
  );
}

export default Footer;
