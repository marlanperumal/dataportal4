// import Swiper from "react-id-swiper";
import Header from "./components/Header";
import Footer from "./components/Footer";
import "./Pricing.css";
import dataPivotsImg from "./assets/images/Home/data-pivots.jpg";
import segmentBuilderImg from "./assets/images/Home/segment-builder.jpg";
import uploadImg from "./assets/images/Home/upload.jpg";
import dashboardsImg from "./assets/images/Home/dashboards.jpg";
import excelExportsImg from "./assets/images/Home/excel-exports.jpg";
import supportImg from "./assets/images/Home/support.jpg";

function Pricing() {
  const params = {
    slidesPerView: 3,
    spaceBetween: 36.5,
    loop: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
      hiddenClass: "swiper-button-hidden",
    },
  };

  const user = {};
  const _forecastingToolInfo = () => {};
  const _segmentBuilderInfo = () => {};
  const _uploadYourOwnDataInfo = () => {};
  const _createYourOwnDashboardsInfo = () => {};
  const _excelExportsInfo = () => {};
  const _customerSupportInfo = () => {};
  return (
    <div id="wrapper">
      {/* {communicationModal} */}
      <Header user={user} screen={"pricing"}></Header>
      <div className="packageItem_container">
        <section id="package_info" className="packageList_container">
          <div className="container-fluid">
            <div className="row">
              <div className="container">
                <div className="row">
                  <div className="col-md-12">
                    <h1 className="packageList_title">
                      Packages &amp; Pricing
                    </h1>
                    <div className="subheading">
                      A comprehensive list of all our Eighty20 Data Portal
                      packages and their associated databases. All packages are
                      supported by the same underlying set of functionality.
                    </div>
                  </div>
                </div>
                <div className="row">
                  <div className="slider4">
                    {/* <Swiper {...params}>
                      <div className="slide">
                        <div className="selected-pricing">
                          <h2>Consumer Portal</h2>
                          <h3>
                            <span className="price">
                              {this.state.consumerPortalPrice}
                            </span>
                            <span className="pmonth">
                              /{this.state.consumerPortalMonth}
                            </span>
                          </h3>
                          <p className="annual">
                            {this.state.consumerPortalTerm}
                          </p>
                          <div className="free-trial-small">
                            <img src="/static/images/Home/free-trial_small.png" />
                          </div>
                        </div>

                        <form action="#" method="post">
                          <select
                            id="lang"
                            onChange={this._onChange}
                            value={this.state.consumerPortalPrice}
                          >
                            <option value="R3,500">R3,500 /month</option>
                            <option value="R4,500">
                              3 Months - R4,500 /month
                            </option>
                            <option value="R7,500">
                              1 Month - R7,500 /month
                            </option>
                            <option value="R10,000">
                              R10,000 /month + retainer
                            </option>
                          </select>
                        </form>

                        <p>
                          <a
                            href="#"
                            className="btn btn-primary"
                            onClick={this._consumerPortalForm}
                          >
                            Enquire Now
                          </a>
                        </p>

                        <div className="data-sets">
                          <table
                            width="100%"
                            cellSpacing="0"
                            cellPadding="0"
                            className="table table-striped"
                          >
                            <tbody>
                              <tr>
                                <td>
                                  <h4>Datasets</h4>
                                </td>
                              </tr>
                              <tr>
                                <td className="black">
                                  Income &amp; Expenditure
                                </td>
                              </tr>
                              <tr>
                                <td className="black">
                                  AMPS (All Meda and Products)
                                </td>
                              </tr>
                              <tr>
                                <td className="black">Labour Force</td>
                              </tr>
                              <tr>
                                <td className="black">
                                  7 More
                                  <a onClick={this._consumerPortalInfo}>
                                    <i className="fa fa-info"></i>
                                  </a>
                                </td>
                              </tr>
                              <tr>
                                <td>&nbsp;</td>
                              </tr>
                              <tr>
                                <td>
                                  <h4>Functionality</h4>
                                </td>
                              </tr>
                              <tr>
                                <td className="black">
                                  Data Tools
                                  <a href="#data-tools">
                                    <i className="fa fa-info"></i>
                                  </a>
                                </td>
                              </tr>
                              <tr>
                                <td>&nbsp;</td>
                              </tr>
                              <tr>
                                <td>
                                  <h4>Support</h4>
                                </td>
                              </tr>
                              <tr>
                                <td className="black">
                                  User Support
                                  <a onClick={this._userSupportInfo}>
                                    <i className="fa fa-info"></i>
                                  </a>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </div>
                      </div>
                      <div className="slide">
                        <div className="selected-pricing">
                          <h2>Credit Portal</h2>
                          <h3>
                            <span className="price">
                              {this.state.creditPortalPrice}
                            </span>
                            <span className="pmonth">
                              /{this.state.creditPortalMonth}{" "}
                            </span>
                          </h3>
                          <p className="annual">
                            {this.state.creditPortalTerm}
                          </p>
                        </div>

                        <form action="#" method="post">
                          <select
                            id="lang"
                            onChange={this._onChange}
                            value={this.state.creditPortalPrice}
                          >
                            <option value="R12,500">R12,500 /month</option>
                            <option value="R15,000">
                              3 Months - R15,000 /month
                            </option>
                            <option value="R20,000">
                              1 Month - R20,000 /month
                            </option>
                          </select>
                        </form>

                        <p>
                          <a
                            href="#"
                            className="btn btn-primary"
                            onClick={this._creditPortalForm}
                          >
                            Enquire Now
                          </a>
                        </p>

                        <div className="data-sets">
                          <table
                            width="100%"
                            cellSpacing="0"
                            cellPadding="0"
                            className="table table-striped"
                          >
                            <tbody>
                              <tr>
                                <td>
                                  <h4>Datasets</h4>
                                </td>
                              </tr>
                              <tr>
                                <td className="black">
                                  XDS Credit Data
                                  <a onClick={this._xdsCreditInfo}>
                                    <i
                                      className="fa fa-info"
                                      aria-hidden="true"
                                    ></i>
                                  </a>
                                </td>
                              </tr>
                              <tr>
                                <td className="black">NCR Credit Data</td>
                              </tr>
                              <tr>
                                <td>&nbsp;</td>
                              </tr>
                              <tr>
                                <td>
                                  <h4>Functionality</h4>
                                </td>
                              </tr>
                              <tr>
                                <td className="black">
                                  Data Tools
                                  <a href="#data-tools">
                                    <i
                                      className="fa fa-info"
                                      aria-hidden="true"
                                    ></i>
                                  </a>
                                </td>
                              </tr>
                              <tr>
                                <td>&nbsp;</td>
                              </tr>
                              <tr>
                                <td>
                                  <h4>Support</h4>
                                </td>
                              </tr>
                              <tr>
                                <td className="black">
                                  User Support
                                  <a onClick={this._userSupportInfo}>
                                    <i
                                      className="fa fa-info"
                                      aria-hidden="true"
                                    ></i>
                                  </a>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </div>
                      </div>
                      <div className="slide">
                        <div className="selected-pricing">
                          <h2>Premium Datasets</h2>
                          <h3>
                            <span className="price">P.O.A</span>{" "}
                            <span className="pmonth">/dataset</span>
                          </h3>
                          <p>&nbsp;</p>
                        </div>

                        <form action="#" method="post">
                          <select>
                            <option value="P.O.A">P.O.A</option>
                          </select>
                        </form>

                        <p>
                          <a
                            href="#"
                            className="btn btn-primary"
                            onClick={this._premiumDatasetsForm}
                          >
                            Enquire Now
                          </a>
                        </p>

                        <div className="data-sets">
                          <table
                            width="100%"
                            cellSpacing="0"
                            cellPadding="0"
                            className="table table-striped"
                          >
                            <tbody>
                              <tr>
                                <td>
                                  <h4>Datasets</h4>
                                </td>
                              </tr>
                              <tr>
                                <td className="black">Tourism</td>
                              </tr>
                              <tr>
                                <td className="black">Education</td>
                              </tr>
                              <tr>
                                <td className="black">African</td>
                              </tr>
                              <tr>
                                <td className="black">
                                  Many more
                                  <a onClick={this._premiumDatasetsInfo}>
                                    <i
                                      className="fa fa-info"
                                      aria-hidden="true"
                                    ></i>
                                  </a>
                                </td>
                              </tr>
                              <tr>
                                <td>&nbsp;</td>
                              </tr>
                              <tr>
                                <td>
                                  <h4>Functionality</h4>
                                </td>
                              </tr>
                              <tr>
                                <td className="black">
                                  Data Tools
                                  <a href="#data-tools">
                                    <i
                                      className="fa fa-info"
                                      aria-hidden="true"
                                    ></i>
                                  </a>
                                </td>
                              </tr>
                              <tr>
                                <td>&nbsp;</td>
                              </tr>
                              <tr>
                                <td>
                                  <h4>Support</h4>
                                </td>
                              </tr>
                              <tr>
                                <td className="black">
                                  User Support
                                  <a onClick={this._userSupportInfo}>
                                    <i
                                      className="fa fa-info"
                                      aria-hidden="true"
                                    ></i>
                                  </a>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </div>
                      </div>
                      <div className="slide">
                        <div className="selected-pricing">
                          <h2>New Data Products</h2>
                          <h3>
                            <span className="price">Coming Soon</span>{" "}
                            <span className="pmonth">/info below</span>
                          </h3>
                          <p>&nbsp;</p>
                        </div>

                        <form action="#" method="post">
                          <select>
                            <option>Coming Soon</option>
                          </select>
                        </form>

                        <p>
                          <a
                            href="#"
                            className="btn btn-primary"
                            onClick={this._premiumDatasetsForm}
                          >
                            Enquire Now
                          </a>
                        </p>

                        <div className="data-sets">
                          <table
                            width="100%"
                            cellSpacing="0"
                            cellPadding="0"
                            className="table table-striped"
                          >
                            <tbody>
                              <tr>
                                <td>
                                  <h4>Datasets</h4>
                                </td>
                              </tr>
                              <tr>
                                <td className="black">Tourism</td>
                              </tr>
                              <tr>
                                <td className="black">Education</td>
                              </tr>
                              <tr>
                                <td>&nbsp;</td>
                              </tr>
                              <tr>
                                <td>
                                  <h4>Functionality</h4>
                                </td>
                              </tr>
                              <tr>
                                <td className="black">
                                  Data Tools
                                  <a href="#data-tools">
                                    <i
                                      className="fa fa-info"
                                      aria-hidden="true"
                                    ></i>
                                  </a>
                                </td>
                              </tr>
                              <tr>
                                <td>&nbsp;</td>
                              </tr>
                              <tr>
                                <td>
                                  <h4>Support</h4>
                                </td>
                              </tr>
                              <tr>
                                <td className="black">
                                  User Support
                                  <a onClick={this._userSupportInfo}>
                                    <i
                                      className="fa fa-info"
                                      aria-hidden="true"
                                    ></i>
                                  </a>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </div>
                      </div>
                    </Swiper> */}
                  </div>
                </div>

                <div className="row mrg-top-lg">
                  <div className="col-md-12">
                    <div className="arrow_box">
                      Call us today to upgrade your account:{" "}
                      <strong>+27 (021) 461 8020</strong>
                    </div>
                  </div>
                </div>

                <div className="row mrg-top-lg">
                  <div className="col-md-12">
                    <h2 className="packageList_title">Features</h2>
                    <div className="subheading">
                      Enjoy all the features, just choose your datasets.
                    </div>
                  </div>
                </div>

                <div className="row" id="data-tools">
                  <div className="spacer"></div>
                  <div className="col-md-4">
                    <div className="feature-border-box">
                      <img src={dataPivotsImg} alt="data-pivots" />
                      <h3>Forecasting &amp; Trending Tools </h3>
                      <p className="black text-left">
                        Use the trending tool to identify and measure trends in
                        the data. Our forecasting tool takes this one step
                        further, using automated linear regression to forecast
                        future statistics based on historical data. Use it to
                        predict the[...]
                      </p>
                      <br />
                      <p>
                        <a
                          className="btn btn-default"
                          onClick={_forecastingToolInfo}
                        >
                          View details »
                        </a>
                      </p>
                    </div>
                  </div>

                  <div className="col-md-4">
                    <div className="feature-border-box">
                      <img src={segmentBuilderImg} alt="segment-builder" />
                      <h3>Segment Builder</h3>
                      <p className="black text-left">
                        Where existing variables and derived fields don't give
                        you the full picture, create your own custom segments
                        and segmentations and look at the data however you want.
                        Create a 'Luxury Vehicle competitors' segment from a
                        list[...]
                      </p>
                      <br />
                      <p>
                        <a
                          className="btn btn-default"
                          onClick={_segmentBuilderInfo}
                        >
                          View details »
                        </a>
                      </p>
                    </div>
                  </div>

                  <div className="col-md-4">
                    <div className="feature-border-box">
                      <img src={uploadImg} alt="upload" />
                      <h3>Upload Your Own Data</h3>
                      <p className="black text-left">
                        In addition to accessing the existing datasets, you can
                        also upload your own data to the portal: Whether from
                        tracking studies, transactional data or whatever other
                        data it might be. There’s no need to learn how to use
                        new[...]
                      </p>
                      <br />
                      <p>
                        <a
                          className="btn btn-default"
                          onClick={_uploadYourOwnDataInfo}
                        >
                          View details »
                        </a>
                      </p>
                    </div>
                  </div>
                </div>

                <div className="row">
                  <div className="col-lg-4">
                    <div className="feature-border-box">
                      <img src={dashboardsImg} alt="dashboards" />
                      <h3>Customisable Dashboards</h3>
                      <p className="black text-left">
                        Build your own story with metrics and visualisations
                        from our datasets (or your own) using our dashboarding
                        functionality. Create multiple dashboards to compare
                        data across time periods, between market[...]
                      </p>
                      <br />
                      <p>
                        <a
                          className="btn btn-default"
                          onClick={_createYourOwnDashboardsInfo}
                        >
                          View details »
                        </a>
                      </p>
                    </div>
                  </div>
                  <div className="col-lg-4">
                    <div className="feature-border-box">
                      <img src={excelExportsImg} alt="excel-exports" />
                      <h3>Excel Exports</h3>
                      <p className="black text-left">
                        Download your data queries straight from the Data Portal
                        into an Excel pivot table or just into a spreadsheet or
                        CSV file. Using the Data Portal plugin for Excel, you
                        can continue to use Data Portal functionality with the
                        data[...]
                      </p>
                      <br />
                      <p>
                        <a
                          className="btn btn-default"
                          onClick={_excelExportsInfo}
                        >
                          View details»
                        </a>
                      </p>
                    </div>
                  </div>
                  <div className="col-lg-4">
                    <div className="feature-border-box">
                      <img src={supportImg} alt="support" />
                      <h3>Eighty20 Support</h3>
                      <p className="black text-left">
                        Eighty20 has been one of South Africa’s most reputable
                        research and data consultancies since 2001 and is home
                        to dozens of statisticians, developers, programmers,
                        mathematicians, researchers and actuar[...]
                      </p>
                      <br />
                      <p>
                        <a
                          className="btn btn-default"
                          onClick={_customerSupportInfo}
                        >
                          View details »
                        </a>
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        {/* {background} */}
      </div>
      <section>
        <Footer></Footer>
      </section>
    </div>
  );
}

export default Pricing;
