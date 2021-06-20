'use strict';

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
   render() {
        return (<a href={"/jobs/" + this.props.id}>{this.props.name}</a>);
    }
}



class JobList extends React.Component {
    constructor(props) {
        super(props);
        this.state = { jobs : [{id: 1,
                                name: "foo"
                               },
                               {id: 2,
                                name: "bar"
                               },
                               {id: 3,
                                name: "baz"
                               }]
                       }
    }
    render() {
        var jobs = this.state.jobs;
        return (<ol>
                {jobs.map(function(item) {return <li key={item.id}> 
                                          <JobItem id={item.id} name={item.name}/>
                                          </li>})}
                </ol>);
    }
}


const domContainer = document.querySelector('#rdemo');
ReactDOM.render(e(LikeButton), domContainer);


const sd = document.querySelector("#joblist");
ReactDOM.render(<JobList name="hello"/>, sd);













