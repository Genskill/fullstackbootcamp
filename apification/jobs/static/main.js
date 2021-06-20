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


class JobList extends React.Component {
    render() {
            return (<div>
                    {this.props.name}
                    </div>);
    }
}


const domContainer = document.querySelector('#rdemo');
ReactDOM.render(e(LikeButton), domContainer);


const sd = document.querySelector("#joblist");
ReactDOM.render(<JobList name="hello"/>, sd);













