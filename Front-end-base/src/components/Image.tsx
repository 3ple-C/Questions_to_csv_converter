const Image = ({...props}) =>{
    
    const {source, altText} = props;

    return <>
        
            <div>
                <img src={source} alt={altText} />
            </div>
    </>
}

export default Image;