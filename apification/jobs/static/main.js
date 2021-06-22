'use strict';

class JobDetail extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        var jobdetails = this.props.jobdetails;
        if (jobdetails) {
            return(<span> 
                   <h4 className="text-muted">{jobdetails.title}</h4>
                   <div className="badge bg-primary">{jobdetails.status}</div>
                   <p>
                   {jobdetails.jd}
                   </p>
                   </span>);
        } else {
            return(<span> Click on a job to see details </span>);
        }
    }
}


class JobList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {jobs : null};
        axios.get("/jobs", {headers: {'Accepts': 'application/json'}})
            .then((resp) =>  {
                this.setState({jobs : resp.data});
            })
            .catch(function(error) {
                console.log(error);
            })
         }
    handleClick(e, job_id, callback) {
        callback(job_id);
        e.preventDefault();
        }
    render() {
        var jobs = this.state.jobs;
        var callback = this.props.callback;
        var handleClick = this.handleClick;
        if (jobs) {
            return (<ol>
                    {jobs.jobs.map(function(item) {
                        return (<li key={item.id}> 
                                <a href={"/jobs/" + item.id} onClick={(e) => handleClick(e, item.id, callback)}>{item.title}</a>
     
                                </li>)})}
                    </ol>);
            } else {
                return (<span> Loading... </span>);
            }
    }
}

class JobInfo extends React.Component {
    constructor(props) {
        super(props);
        this.state = {jobs: [],
                      current: null};
        this.updateCurrentJob = this.updateCurrentJob.bind(this);
    }
    updateCurrentJob(job_id) {
        const jobs = this.state.jobs.slice();
        axios.get("/jobs/"+job_id, 
                  {headers: {'Accepts': 'application/json'}})
            .then((resp) =>  {
                this.setState({jobs: jobs,
                               current : {title : resp.data.title,
                                          company : resp.data.company,
                                          status : resp.data.status,
                                          jd : resp.data.jd}});
            })
            .catch(function(error) {
                console.log("Error " , error);
                this.setState({jobs: jobs,
                               current : {title: "Error",
                                          company: "Error",
                                          status : "Error",
                                          jd: "Error"}});
            })
        }
    render() {
        return (
            <div className="row">
                <div className="col-3 sidebar">
                <h2> Stats </h2>
                <ul>
                <li> Last crawled -  </li>
                <li> Total jobs in system - </li>
                </ul>
                <JobList callback={(job_id) => this.updateCurrentJob(job_id)}/>
                </div>

                <div className="col-7">
                <JobDetail jobdetails={this.state.current}/>
                </div>
                </div>

        );
    }
}


const cont = document.querySelector("#jobinfo");
ReactDOM.render(<JobInfo/>, cont);




