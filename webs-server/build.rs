fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Compile all .proto files from the shared proto/ directory.
    tonic_build::configure()
        .build_server(true)
        .build_client(false)
        .compile(
            &[
                "../proto/auth.proto",
                "../proto/feed.proto",
                "../proto/post.proto",
                "../proto/spins.proto",
                "../proto/profile.proto",
                "../proto/circles.proto",
                "../proto/stories.proto",
                "../proto/messages.proto",
                "../proto/activity.proto",
                "../proto/search.proto",
            ],
            &["../proto"],
        )?;
    Ok(())
}
