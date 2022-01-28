export const getInCompleteTasks = (tasks) => {
    let res = tasks.filter(t => t.status !== 'Done')
    return res
}

export const getCompleteTasks = (tasks) => {
    let res = tasks.filter(t => t.status === 'Done')
    return res
}

export const getDate = () => {
    return new Date().toDateString()
}