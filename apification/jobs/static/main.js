'use strict';
// const axios = require('axios');

const e = React.createElement;

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    if (this.state.liked) {
      return 'You liked this.';
    }

    return e(
      'button',
      { onClick: () => this.setState({ liked: true }) },
      'Like'
    );
  }
}


class JobItem extends React.Component {
    fetchItem(e, job_id) {
        axios.get("/jobs/"+job_id,   {headers: {'Accepts': 'application/json'}})
        .then(function(resp) {
                console.log(resp);
        })
        .catch(function(error) {
            console.log(error);
        })
        e.preventDefault();
    }

    render() {
        return (<a href={"/jobs/" + this.props.id} onClick={(e)=>this.fetchItem(e,this.props.id)}>{this.props.name}</a>);
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
    render() {
        var jobs = this.state.jobs;
        console.log("Running ");
        if (jobs) {
            return (<ol>
                    {jobs.jobs.map(function(item) {
                             return (<li key={item.id}> 
                            <JobItem id={item.id} name={item.title}/>
                            </li>)})}
                    </ol>);
            } else {
                return (<span> Loading... </span>);
            }
    }
}


const domContainer = document.querySelector('#rdemo');
ReactDOM.render(e(LikeButton), domContainer);


const sd = document.querySelector("#joblist");
ReactDOM.render(<JobList name="hello"/>, sd);













